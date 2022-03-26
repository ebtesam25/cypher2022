module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  themes: [
    {
      immigrace: {
      
"primary": "#1E698D",
      
"secondary": "#F0BB29",
      
"accent": "#1E698E",
      
"neutral": "#F0BB19",
      
"base-100": "#FFFFFF",
      
"info": "#3ABFF8",
      
"success": "#36D399",
      
"warning": "#FBBD23",
      
"error": "#F87272",
      },
    },
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}