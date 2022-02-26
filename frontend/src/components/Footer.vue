<template>
  <footer>
    <div class="row copyright">
      <div class="footer-menu">
        <a href="">Home</a>
        <a href="">About</a>
      </div>
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
  padding: 0.3em 1em;
  background-color: #25262e;
}
.footer-menu {
  float: left;
  margin-top: 10px;
}

.footer-menu a {
  color: #cfd2d6;
  padding: 6px;

  text-decoration: none;
}
.footer-menu a:hover {
  color: #27bcda;
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
