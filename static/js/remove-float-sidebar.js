// remove-float-sidebar.js
(function() {
    'use strict';

    function nuclearRemove() {
        const selectors = [
            '.float-sidebar',
            '[data-mod-id="allSet[0]"]',
            '.chat-assistant',
            '.float-bar-ad',
            '.float-config-btn',
            '.float-bar-nav'
        ];

        selectors.forEach(selector => {
            const elements = document.querySelectorAll(selector);
            elements.forEach(el => el.remove());
        });

        const observer = new MutationObserver(function(mutations) {
            mutations.forEach(function(mutation) {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) {
                        if (node.classList && (
                            node.classList.contains('float-sidebar') ||
                            node.getAttribute('data-mod-id') === 'allSet[0]'
                        )) {
                            node.remove();
                        }
                    }
                });
            });
        });

        observer.observe(document.body, { childList: true, subtree: true });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', nuclearRemove);
    } else {
        nuclearRemove();
    }

    setInterval(nuclearRemove, 300);
})();
