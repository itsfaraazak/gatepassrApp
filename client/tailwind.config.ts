/** @type {import('tailwindcss').Config} */

import { join } from 'path';
import type { Config } from 'tailwindcss';

import { skeleton } from '@skeletonlabs/tw-plugin';

import plugin from 'tailwindcss/plugin';

const config = {
	// 2. Opt for dark mode to be handled via the class method
	darkMode: 'class',
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		// 3. Append the path to the Skeleton package
		join(require.resolve(
			'@skeletonlabs/skeleton'),
			'../**/*.{html,js,svelte,ts}'
		)
	],
	theme: {
		extend: {},
	},
	plugins: [
		// 4. Append the Skeleton plugin (after other plugins)
    require('@tailwindcss/forms'),
    plugin(function({ addUtilities }){
      const newUtilities = {
          '.safe-top' : {
              paddingTop: 'constant(safe-area-inset-top)',
              paddingTop: 'env(safe-area-inset-top)'
          },
          '.safe-left' : {
              paddingLeft: 'constant(safe-area-inset-left)',
              paddingLeft: 'env(safe-area-inset-left)'
          },
          '.safe-right' : {
              paddingRight: 'constant(safe-area-inset-right)',
              paddingRight: 'env(safe-area-inset-right)'
          },
          '.safe-bottom' : {
              paddingBottom: 'constant(safe-area-inset-bottom)',
              paddingBottom: 'env(safe-area-inset-bottom)'
          }
      }

      addUtilities( newUtilities );
    }),

		skeleton({
      themes: { preset: [
        // Enabling enhancements
        { name: "skeleton", enhancements: true}
        
      ] }
    })
    
	]
} satisfies Config;


export default config;



/* 
export default {
  content: ['./src/**/ /*.{html,js,svelte,ts}'],
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
    plugin(function({ addUtilities }){
      const newUtilities = {
          '.safe-top' : {
              paddingTop: 'constant(safe-area-inset-top)',
              paddingTop: 'env(safe-area-inset-top)'
          },
          '.safe-left' : {
              paddingLeft: 'constant(safe-area-inset-left)',
              paddingLeft: 'env(safe-area-inset-left)'
          },
          '.safe-right' : {
              paddingRight: 'constant(safe-area-inset-right)',
              paddingRight: 'env(safe-area-inset-right)'
          },
          '.safe-bottom' : {
              paddingBottom: 'constant(safe-area-inset-bottom)',
              paddingBottom: 'env(safe-area-inset-bottom)'
          }
      }

      addUtilities( newUtilities );
    })
  ],
}


 */