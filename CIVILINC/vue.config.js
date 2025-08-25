const path = require('path')

module.exports = {
  runtimeCompiler: true, // Enable runtime compiler for template compilation
  devServer: {
    allowedHosts: "all",
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_URL || 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': '' // Remove /api from the path when forwarding to backend
        },
        logLevel: 'debug' // Enable proxy logging
      }
    },
    client: {
      overlay: {
        warnings: false,
        errors: true
      }
    }
  },
  configureWebpack: {
    resolve: {
      alias: {
        'vue$': 'vue/dist/vue.esm.js' // Use the full build with template compiler
      }
    }
  },
  css: {
    loaderOptions: {
      css: {
        url: false,
      },
    },
  },
  chainWebpack: config => {
    config.plugin('copy').tap(args => {
      const UNESCAPED_GLOB_SYMBOLS_RE = /(\\?)([()*?[\]{|}]|^!|[!+@](?=\())/g;
      const publicDir = path.resolve(process.VUE_CLI_SERVICE.context, 'public').replace(/\\/g, '/');
      const escapePublicDir= publicDir.replace(UNESCAPED_GLOB_SYMBOLS_RE, '\\$2');
      args[0].patterns[0].globOptions.ignore = args[0].patterns[0].globOptions.ignore.map(i => i.replace(publicDir, escapePublicDir));
      return args;
    });
  }
};