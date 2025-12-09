<script>
	import Header from "./components/Header.svelte";
	import Hero from "./components/Hero.svelte";
	import WhatIsIt from "./components/WhatIsIt.svelte";
	import WhyItMatters from "./components/WhyItMatters.svelte";
	import DataSection from "./components/DataSection.svelte";
</script>

<!-- Sticky Header -->
<Header />

<main class="text-white">
	<!-- Hero Section -->
	<section id="hero" class="border-b border-white/50">
		<Hero />
	</section>

	<!-- What Is It Section -->
	<section id="what-is">
		<WhatIsIt />
	</section>

	<!-- Why It Matters Section -->
	<section id="why-it-matters">
		<WhyItMatters />
	</section>

	<!-- Data Section -->
	<section id="data">
		<DataSection />
	</section>
</main>
