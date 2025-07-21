const path = require("path")
const webpack = require("webpack") // eslint-disable-line no-unused-vars
const MiniCssExtractPlugin = require("mini-css-extract-plugin")
const BundleTracker = require("webpack-bundle-tracker")

const config = {
  context: __dirname,
  entry: {
    main: "./yourcity/static/js/main.js",
    styles: "./yourcity/static/scss/main.scss"
  },
  output: {
    path: path.resolve(__dirname, "assets/bundles/"),
    filename: "[name]-[hash].js",
    chunkFilename: "[name]-[hash].js",
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].bundle.css"
    }),
    new BundleTracker({
      path: __dirname,
      filename: "webpack-stats.json",
    }),
  ],
  devServer: {
    watchFiles: ["{{cookiecutter.module_name}}/static/**/*.js"],
    host: "0.0.0.0",
    port: 3000,
    compress: false,
    allowedHosts: ["localhost"],
  },
  watchOptions: {
    poll: 1000,
  },
  resolve: {
    extensions: [".js", ".scss"],
  },
  ignoreWarnings: [
    {
      module: /sass-loader/, // A RegExp
    },
    /warning from compiler/,
    () => true,
  ],
  module: {
    rules: [
      {
        test: /\.(js)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env"],
        },
      },
      {
        test: /\.(scss)$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ],
      },
    ],
  },
}

module.exports = (env, argv) => {
  /*
   * /app/webpack-stats.json is the roadmap for the assorted chunks of JS
   * produced by Webpack. During local development, the Webpack server
   * serves our bundles. In production, Django should look in
   * /app/static/bundles for bundles.
   */
  if (argv.mode === "development") {
    config.output.publicPath = "http://localhost:3000/static/bundles/"
  }

  if (argv.mode === "production") {
    config.output.publicPath = "/static/bundles/"
  }

  return config
}
