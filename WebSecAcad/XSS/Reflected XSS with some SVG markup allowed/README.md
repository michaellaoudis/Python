# XSS Testing: Enumerate Accepted HTML Tags and Events

## Overview

- This Python script automates the process for finding HTML tag and event pairs accepted by the target web application. A pair is considered accepted (e.g. `<svg animatetransform>`) if it returns a `200 OK` response. Having found an accepted pair, the tester would then manually inject a JavaScript event into the pair to test for XSS at the target URL's search parameter.

- A time delay of `2` seconds is set between each request to avoid flooding the target web server too quickly

- In PortSwigger's Web Security Academy lab at https://portswigger.net/web-security/cross-site-scripting/contexts/lab-some-svg-markup-allowed, the search parameter was vulnerable to Reflected XSS with the following payload:

    `<svg><animatetransform onbegin=alert(1)`
<br></br>

        https://YOUR-LAB-ID.web-security-academy.net/?search=%22%3E%3Csvg%3E%3Canimatetransform%20onbegin=alert(1)%3E

<hr>

## Script Flow
1. Open two text files, where `File 1` contains HTML tags and `File 2` HTML events
2. Send a `GET` request for every tag to the target URL's search parameter

<br>

Example tag `<b>`:

    https://YOUR-LAB-ID.web-security-academy.net/?search=%3Cb%3E

<br>

3. On `200 OK` response, collect the accepted tag
4. Send a `GET` request for every accepted tag to be tested for accepted HTML events (as a pair)

<br>

Example pair `<svg animatetransform>`:

    https://YOUR-LAB-ID.web-security-academy.net/?search=%3Csvg%20animatetransform%3E

<br>

5. On `200 OK` response, collect the accepted pair
6. Sample Output:

        Accepted pair: <svg animatetransform>
        Accepted pair: <title onload>
