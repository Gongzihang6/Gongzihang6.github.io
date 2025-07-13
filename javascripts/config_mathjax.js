window.MathJax = {
    tex: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true,
        packages: {'[+]': ['tagformat', 'mathtools', 'mhchem']}
    },
    options: {
        ignoreHtmlClass: '.*|',
        processHtmlClass: 'arithmatex'
    },
    loader: {
        load: ['[tex]/tagformat', '[tex]/mathtools', '[tex]/mhchem']
    }
};