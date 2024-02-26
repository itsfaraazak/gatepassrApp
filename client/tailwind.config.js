/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    fontFamily: {
      'sans': ['IBM\\ Plex\\ Sans', 'Helvetica\\ Neue', 'Arial', 'sans-serif'],
      'serif': ['IBM\\ Plex\\ Serif', 'Georgia', 'Times', 'serif']
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

