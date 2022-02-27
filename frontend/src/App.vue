<template>
  <div id="app">
    <nav-bar />
    <question-component />
    <footer-component />
  </div>
</template>

<script>
import NavBar from './components/Navbar.vue';
import QuestionComponent from './components/Question.vue';
import FooterComponent from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    QuestionComponent,
    FooterComponent,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
</style>
