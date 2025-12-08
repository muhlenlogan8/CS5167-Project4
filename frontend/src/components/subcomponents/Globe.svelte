<script>
	let videoSrc = "/2-135653517.mp4";
	let videoSrc2 = "BlackMarble_2016_rotate_1080p.mov";
</script>

<div class="relative flex justify-center items-center">
	<!-- Outer Glow -->
	<div class="absolute flex items-center justify-center">
		<div
			class="w-[800px] h-[800px] rounded-full bg-blue-600/20 blur-3xl opacity-40"
		></div>
	</div>

	<!-- Inner Glow -->
	<div class="absolute flex items-center justify-center">
		<div
			class="w-[480px] h-[480px] rounded-full bg-blue-400/10 blur-xl opacity-60"
		></div>
	</div>

	<!-- Globe Video -->
	<div
		class="relative w-[500px] h-[500px] rounded-full overflow-hidden"
		style="
      mask-image: radial-gradient(circle, white 72%, transparent 100%);
      -webkit-mask-image: radial-gradient(circle, white 72%, transparent 100%);
    "
	>
		<video
			src={videoSrc}
			class="w-full h-full object-cover scale-[1.18] brightness-180 contrast-125"
			autoplay
			muted
			loop
			playsinline
		></video>
	</div>
</div>
