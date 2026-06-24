// Some modifications to the base theme
// * preserve sidebar positions when scrolling and clicking somewhere.
//   --> TODO: not working well in Firefox (works fine in Brave)
//   Nor Gemini 3.1 Pro or Sonnet 3.6 seem to be able to completely fix it, so leaving
//   it for the future.
// * make sidebar headers (captions) clickable. Target file is the index of the section.


document.addEventListener("DOMContentLoaded", function() {
    // Preserve sidebar scroll position
    const sidebar = document.querySelector(".sphinxsidebarwrapper");
    if (sidebar) {
        const savedScrollTop = sessionStorage.getItem("sidebarScrollTop");
        if (savedScrollTop) {
            sidebar.scrollTop = parseInt(savedScrollTop, 10);
        }
        window.addEventListener("beforeunload", () => {
            if (sidebar.scrollTop > 0) {
                sessionStorage.setItem("sidebarScrollTop", sidebar.scrollTop);
            } else {
                sessionStorage.removeItem("sidebarScrollTop");
            }
        });
    }

    // Map your sidebar captions exactly as they appear, to their target files
    const captionLinks = {
        "Start here": "getting-started/index.html",
        "Howto guides": "howtos/index.html",
        "User reference": "reference/index.html",
        "Help and support": "help/index.html",
        "Other resources": "others/index.html",
        "Advanced topics": "advanced/index.html",
        "Technical documentation": "technical/index.html"
    };

    // Sphinx puts the captions inside <span class="caption-text"> inside <p class="caption">
    const captions = document.querySelectorAll("p.caption > span.caption-text");

    // Modern Sphinx stores the path back to root here (e.g., "./" or "../../")
    const rootPath = document.documentElement.dataset.content_root || "./";

    captions.forEach(span => {
        const title = span.textContent.trim();

        if (captionLinks[title]) {
            // Build the URL relative to the current page's depth
            const targetUrl = rootPath + captionLinks[title];

            // Replicate standard styling so it doesn't look out of place
            span.style.cursor = "pointer";
            span.style.transition = "color 0.2s ease-in-out";

            // Optional hover effect
            span.onmouseover = () => span.style.color = "var(--ai4Color_inv)";
            span.onmouseout = () => span.style.color = "inherit";

            // Navigate on click (bypassing any global <a> tag interceptors)
            span.onclick = (e) => {
                e.stopPropagation();
                window.location.href = targetUrl;
            };
        }
    });
});