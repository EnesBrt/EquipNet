/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./cmdb_app/**/*.{html,js}",
  ],
  
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ]
}