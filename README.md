<script src="https://cdnjs.cloudflare.com/ajax/libs/clipboard.js/2.0.8/clipboard.min.js"></script>
<!-- Добавьте этот код там, где вы хотите разместить кнопку копирования -->
<button class="btn" data-clipboard-target="#copy-target">Copy</button>
<div id="copy-target">
  <!-- Ваш текст, который вы хотите скопировать -->
  Пример текста для копирования.
</div>

<script>
  var clipboard = new ClipboardJS('.btn');
</script>
