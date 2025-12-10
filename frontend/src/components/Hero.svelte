<script>
	import Globe from "./subcomponents/Globe.svelte";
</script>

<section
	class="flex items-center p-25 bg-[#131418] overflow-hidden"
>
	<div class="w-full grid grid-cols-2 gap-16 items-center">
		<!-- Globe -->
		<div class="flex justify-center">
			<Globe />
		</div>

		<!-- Text Stuff -->
		<div class="space-y-6 text-left">
			<h1 class="text-5xl font-bold leading-tight">
				<span class="text-white">Global</span>
				<span
					class="bg-linear-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent"
					>Energy Inequality</span
				> <br />
				<span class="text-white">and</span>
				<span
					class="bg-linear-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent"
					>Energy Poverty</span
				>
			</h1>

			<p class="text-gray-300 text-xl max-w-lg mx-0">
				Over <span class="text-cyan-400 font-bold">1.1 billion</span> people live
				in energy poverty without reliable, affordable, and modern energy services. Access
				to electricity shapes health, education, safety, and opportunity.
			</p>
		</div>
	</div>
</section>
