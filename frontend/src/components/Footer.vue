<template>
  <footer>
    <div class="row copyright">
      <p>Copyright &copy; 2022 Burak Saglam</p>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent',
  data() {
    return {};
  },
};
</script>

<style scoped>
footer {
  background-color: #121315;
  color: #a7a7a7;
  font-size: 16px;
  position: fixed;
  bottom: 0;
  min-width: 100vw;
}
footer * {
  font-family: 'Poppins', sans-serif;
  box-sizing: border-box;
  border: none;
  outline: none;
}
.row {
  padding: 1em 1em;
}
.row.primary {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  align-items: stretch;
}
.copyright {
  background-color: #25262e;
}
.copyright p {
  font-size: 0.9em;
  text-align: right;
}
@media screen and (max-width: 850px) {
  .row.primary {
    grid-template-columns: 1fr;
  }
}
</style>
