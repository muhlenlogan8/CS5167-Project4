<script>
	import EnergyScatter from "./subcomponents/ScatterPlot.svelte";
	import Map from "./subcomponents/Map.svelte";
</script>

<section id="scatter" class="py-20 px-20 bg-[#1d1f25] space-y-2">
	<h2 class="text-4xl font-bold text-center text-white">
		Energy Use vs. Life Expectancy
	</h2>

	<p class="text-gray-300 max-w-2xl mx-auto text-center py-4">
		Countries using more energy per capita tend to exhibit significantly higher
		life expectancy.
	</p>

	<EnergyScatter />
	<p class="text-gray-300 max-w-3xl mx-auto text-center">
		Plot based on the visual from <a
			href="https://visualizingenergy.org/does-more-energy-use-increase-life-expectancy/"
			class="underline text-cyan-400 hover:text-cyan-300"
			>visualizingenergy.org</a
		> and data from the World Bank and Our World in Data
	</p>
</section>
