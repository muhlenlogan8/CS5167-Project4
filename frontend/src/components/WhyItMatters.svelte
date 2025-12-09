<script>
	import { fade } from "svelte/transition";

	let isOn = $state(false);

	const offInfo = [
		{
			title: "No Reliable Electricity",
			text: "685 million people live without any electricity access (2022), reversing years of progress.",
		},
		{
			title: "Unsafe Indoor Air",
			text: "3.2 million people die annually from indoor air pollution caused by cooking with wood, charcoal, or dung.",
		},
		{
			title: "Limited Education",
			text: "Students in energy-poor households lose hours of study time every night due to lack of lighting.",
		},
		{
			title: "Healthcare Barriers",
			text: "Clinics without reliable power cannot refrigerate vaccines or operate essential medical equipment.",
		},
	];

	const onInfo = [
		{
			title: "Power for Education",
			text: "Nighttime lighting increases study hours and improves literacy rates in electrified communities.",
		},
		{
			title: "Health + Safety",
			text: "Reliable energy enables vaccine refrigeration, safe childbirth, and reduces indoor air pollution.",
		},
		{
			title: "Economic Opportunity",
			text: "Electricity enables refrigeration, machinery, digital access, and increases income opportunities.",
		},
		{
			title: "Community Well-Being",
			text: "Public lighting improves safety and empowers community development.",
		},
	];

	function toggle() {
		isOn = !isOn;
	}
</script>

<section
	class="py-20 px-20 transition-colors duration-700"
	class:bg-[#1d1f25]={!isOn}
	class:bg-[#e7e7e7]={isOn}
>
	<div class="max-w-7xl mx-auto">
		<div class="grid grid-cols-2 gap-16 items-center">
			<!-- Left Switch -->
			<div class="space-y-12">
				<h2
					class="text-4xl font-bold text-center"
					class:text-white={!isOn}
					class:text-gray-900={isOn}
				>
					{isOn ? "With" : "Without"} Modern Energy
				</h2>

				<!-- Switch -->
				<div class="flex justify-center items-center">
					<button
						type="button"
						class="relative w-24 h-12 rounded-full bg-gray-300 cursor-pointer focus:outline-none focus:ring-2 focus:ring-blue-400 transition-colors duration-300"
						aria-pressed={isOn}
						aria-label="Toggle energy mode"
						onclick={toggle}
					>
						<!-- Knob Component -->
						<div
							class="absolute top-1/2 -translate-y-1/2 w-10 h-10 rounded-full bg-white shadow transition-all duration-300"
							style="left: {isOn ? 'calc(100% - 44px)' : '4px'}"
						></div>
					</button>
				</div>
			</div>

			<!-- Right Facts -->
			<div class="grid grid-cols-1 gap-6">
				{#each isOn ? onInfo : offInfo as fact}
					<div
						in:fade={{ duration: 300 }}
						out:fade={{ duration: 200 }}
						class="p-6 rounded-xl border
                         {isOn
							? 'bg-white/80 border-gray-200 text-gray-800'
							: 'bg-white/5 border-white/10 text-gray-200'}"
					>
						<h3 class="text-xl font-semibold mb-2 text-blue-400">
							{fact.title}
						</h3>
						<p>{fact.text}</p>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>
