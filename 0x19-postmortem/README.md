# Incident Analysis

Following the deployment of ALX's System Engineering & DevOps project 0x19 at approximately 06:00 West African Time (WAT) in Nigeria, an outage took place on an isolated Ubuntu 14.04 container running an Apache web server. Users attempting GET requests encountered unexpected `500 Internal Server Error` responses instead of the anticipated HTML file defining a simple Holberton WordPress site.

## Troubleshooting Process

Upon encountering the issue at roughly 19:20 PST, Brennan (nicknamed BDB) initiated the debugging process:

1. Inspected running processes using `ps aux`, confirming two `apache2` processes - `root` and `www-data` - were functioning correctly.

2. Explored the `/etc/apache2/sites-available` directory to ascertain that the web server was serving content from `/var/www/html/`.

3. Employed `strace` on the PID of the `root` Apache process in one terminal while executing a `curl` command in another. Unfortunately, `strace` yielded no actionable insights.

4. Repeated the previous step on the `www-data` process, yielding fruitful results: `strace` exposed an `-1 ENOENT (No such file or directory)` error linked to an attempt to access `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. Conducted a manual search through files in `/var/www/html/` using Vim pattern matching, successfully identifying the erroneous `.phpp` file extension within `wp-settings.php` (specifically on Line 137).

6. Rectified the issue by removing the extraneous `p` from the line.

7. Confirmed resolution by performing another `curl` test on the server, which returned a successful status code (200).

8. Automated the fix by crafting a Puppet manifest to address the typo.

## Summary

In essence, the outage stemmed from a simple typo. Specifically, the WordPress application encountered a critical error in `wp-settings.php` due to an attempt to load `class-wp-locale.phpp`, whereas the correct filename, located in the `wp-content` directory, should have been `class-wp-locale.php`. The remedy involved straightforward correction of the typo by removing the surplus `p`.

## Preventive Measures

This incident underscores the importance of proactive measures to avert similar outages:

- **Thorough Testing**: Conduct rigorous testing of the application prior to deployment to catch potential errors like the one experienced here.

- **Monitoring**: Implement uptime-monitoring services such as [UptimeRobot](https://uptimerobot.com/) to promptly detect and alert stakeholders to any website outages.

In response to this incident, a Puppet manifest ([0-strace_is_your_friend.pp](https://github.com/abdelhafid-mahmoudi-env/alx-system_engineering-devops/blob/master/0x17-web_stack_debugging_3/0-strace_is_your_friend.pp)) was developed to automatically rectify identical errors in the future. This manifest replaces any instances of `phpp` extensions in `/var/www/html/wp-settings.php` with `php`. However, it is paramount to maintain vigilance in testing and monitoring to mitigate the risk of recurrence. After all, even programmers are not immune to errors! 😉
