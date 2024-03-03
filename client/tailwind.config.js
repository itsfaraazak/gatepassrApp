/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    fontFamily: {
      'sans': ['Inter', 'ui-sans-serif', 'system-ui'],
      'serif': ['Inter', 'ui-serif', 'Georgia'],
      'mono': ['Inter', 'ui-monospace', 'SFMono-Regular'],
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

