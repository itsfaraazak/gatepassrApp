import adapter from '@sveltejs/adapter-static';
//import adapter from '@sveltejs/adapter-auto';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: vitePreprocess(),

	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: 'app.html',
			precompress: false,
			strict: true}),
		alias: {
			$components: "src/components",
			$baseurl:"https://itsfaraazak.github.io/gatepassrApp"
			},
		paths: {
			// @ts-ignore
			base: process.argv.includes('dev') ? '' : process.env.BASE_PATH
		}
	}
};

export default config;
