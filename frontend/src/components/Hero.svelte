<script>
	import Globe from "./subcomponents/Globe.svelte";
</script>

<section
	class="min-h-220 flex items-center px-20 pt-32 pb-20 bg-[#131418]"
>
	<div class="w-full grid grid-cols-2 gap-16 items-center">
		<!-- Globe -->
		<div class="flex justify-center">
			<Globe />
		</div>

		<!-- Text Stuff -->
		<div class="space-y-6 text-left">
			<h1 class="text-5xl font-bold leading-tight">
				Illuminating Global <br />
				<span class="text-blue-400">Energy Inequality</span>
			</h1>

			<p class="text-gray-300 text-xl max-w-lg mx-0">
				Across the world, electricity access determines who can study, who can
				work, who can heal — and who falls behind. This interactive experience
				visualizes energy inequality, its impacts, and the pathways forward.
			</p>

			<a
				href="#what-is-energy"
				class="inline-block bg-blue-500 hover:bg-blue-600 text-white font-semibold px-6 py-3 rounded-xl shadow-lg transition"
			>
				Learn More
			</a>
		</div>
	</div>
</section>
