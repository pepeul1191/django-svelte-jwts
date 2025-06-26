import '../stylesheets/styles.css';
import '../stylesheets/access.css';
import Access from '../components/layouts/Access.svelte';

const app = new Access({
	target: document.body,
	props: {}
});

export default app;