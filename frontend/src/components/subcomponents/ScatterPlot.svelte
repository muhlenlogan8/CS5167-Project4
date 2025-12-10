<script>
	import { onMount } from "svelte";
	import Chart from "chart.js/auto";
	import dataset from "../../data/scatter_data.json";

	let canvasRef;

	// Continent colors
	const colors = {
		Africa: "rgba(59,130,246,0.7)",
		Asia: "rgba(234,179,8,0.7)",
		Europe: "rgba(168,85,247,0.7)",
		"North America": "rgba(34,197,94,0.7)",
		"South America": "rgba(249,115,22,0.7)",
		Oceania: "rgba(14,165,233,0.7)",
	};

	onMount(() => {
        // Create points data for chart
		const points = dataset.map((data) => ({
			x: data.energy_gj,
			y: data.life_expectancy,
			label: data.country,
			continent: data.continent,
			backgroundColor: colors[data.continent] ?? "rgba(255,255,255,0.7)",
		}));

		new Chart(canvasRef, {
			type: "scatter",
			data: {
				datasets: [
					{
						label: "Countries",
						data: points,
						pointRadius: 6,
						pointHoverRadius: 10,
						borderWidth: 1,
						borderColor: (ctx) => ctx.raw.backgroundColor,
						backgroundColor: (ctx) => ctx.raw.backgroundColor,
					},
				],
			},
			options: {
				responsive: true,
				plugins: {
					tooltip: {
						callbacks: {
							label: (ctx) => {
								const data = ctx.raw;
								return `${data.label} — ${data.x} GJ per capita, ${data.y} yrs`;
							},
						},
					},
					legend: { display: false },
				},
				scales: {
					x: {
						title: {
							display: true,
							text: "Energy Use per Capita (GJ)",
							color: "#ccc",
						},
						ticks: { color: "#aaa" },
						grid: { color: "rgba(255,255,255,0.05)" },
					},
					y: {
						title: {
							display: true,
							text: "Life Expectancy (Years)",
							color: "#ccc",
						},
						ticks: { color: "#aaa" },
						grid: { color: "rgba(255,255,255,0.05)" },
					},
				},
			},
		});
	});
</script>

<div class="flex flex-wrap gap-6 justify-center">
	{#each Object.keys(colors) as cont}
		<div class="flex items-center space-x-2">
			<div
				class="w-4 h-4 rounded-full"
				style="background-color: {colors[cont]}"
			></div>
			<span class="text-gray-300 text-sm">{cont}</span>
		</div>
	{/each}
</div>

<div
	class="bg-white/5 border border-white/10 px-8 pt-8 pb-4 rounded-xl shadow-xl justify-center max-w-4xl mx-auto"
>
	<canvas bind:this={canvasRef} class="w-full h-[400px]"></canvas>
</div>
