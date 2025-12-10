<script>
	import EnergyScatter from "./subcomponents/ScatterPlot.svelte";

	let selectedMap = $state("energy");

	const maps = {
		energy: {
			title: "Energy Use",
			description:
				"Global energy consumption per capita measured in gigajoules (GJ).",
			img: "/Energy.png",
		},
		life: {
			title: "Life Expectancy",
			description:
				"Average life expectancy in years across countries.",
			img: "/Life.png",
		},
		gdp: {
			title: "GDP",
			description:
				"Gross Domestic Product per capita showing economic development.",
			img: "/GDP.png",
		},
	};
</script>

<section id="scatter" class="pt-10 pb-10 px-20 bg-[#1d1f25] space-y-2">
	<h2 class="text-4xl font-bold text-center text-white p-2">
		Energy Use vs. Life Expectancy
	</h2>

	<!-- <p class="text-gray-300 max-w-2xl mx-auto text-center p-2">
		Countries using more energy per capita tend to exhibit significantly higher
		life expectancy.
	</p> -->

	<EnergyScatter />
	<p class="text-gray-300 max-w-3xl mx-auto text-center">
		Plot based on the visual from <a
			href="https://visualizingenergy.org/does-more-energy-use-increase-life-expectancy/"
			class="underline text-cyan-400 hover:text-cyan-300"
			target="_blank"
			rel="noopener noreferrer">visualizingenergy.org</a
		> and data from the World Bank and Our World in Data
	</p>
</section>

<section id="maps" class="px-20 bg-[#1d1f25] space-y-2">
	<h2 class="text-4xl font-bold text-center text-white">
		Global {maps[selectedMap].title}
	</h2>

	<p class="text-gray-300 max-w-2xl mx-auto text-center py-2">
		{maps[selectedMap].description}
	</p>

	<div
		class="bg-white/5 border border-white/10 px-8 pt-8 pb-4 rounded-xl shadow-xl max-w-4xl mx-auto"
	>
		<!-- Buttons -->
		<div class="flex justify-end gap-3 mb-6">
			<button
				onclick={() => (selectedMap = "energy")}
				class="px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-300 z-20 {selectedMap ===
				'energy'
					? 'bg-white/5 border border-pink-400 text-pink-400 shadow-lg'
					: 'bg-white/5 text-gray-400 hover:bg-white/10 border border-white/10 hover:border-pink-400 hover:text-pink-400'}"
			>
				Energy Use
			</button>

			<button
				onclick={() => (selectedMap = "life")}
				class="px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-300 z-20 {selectedMap ===
				'life'
					? 'bg-white/5 border border-cyan-400 text-cyan-400 shadow-lg'
					: 'bg-white/5 text-gray-400 hover:bg-white/10 border border-white/10 hover:border-cyan-400 hover:text-cyan-400'}"
			>
				Life Expectancy
			</button>

			<button
				onclick={() => (selectedMap = "gdp")}
				class="px-4 py-2 rounded-lg text-sm font-semibold transition-all duration-300 z-20 {selectedMap ===
				'gdp'
					? 'bg-white/5 border border-blue-400 text-blue-400 shadow-lg'
					: 'bg-white/5 text-gray-400 hover:bg-white/10 border border-white/10 hover:border-blue-400 hover:text-blue-400'}"
			>
				GDP
			</button>
		</div>

		<!-- Static Map Image -->
		<img
			src={maps[selectedMap].img}
			alt={maps[selectedMap].title}
			class="w-full rounded-lg -mt-15 z-10"
		/>
	</div>

	<p class="text-gray-300 max-w-3xl mx-auto text-center">
		Data from <a
			href="https://data.worldbank.org/"
			class="underline text-cyan-400 hover:text-cyan-300"
			target="_blank"
			rel="noopener noreferrer">The World Bank</a
		>
		and
		<a
			href="https://ourworldindata.org/grapher/energy-use-per-person-vs-gdp-per-capita"
			class="underline text-cyan-400 hover:text-cyan-300"
			target="_blank"
			rel="noopener noreferrer">Our World in Data</a
		>
	</p>
</section>
