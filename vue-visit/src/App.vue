<template>
  <the-nav></the-nav>
    <router-view name="default"></router-view> 
</template>
<script>
import TheNav from './components/UI/TheNav.vue';
export default {
  components: {
    TheNav
  },
}

</script>


<style>
input, select, textarea {
    border: 1px solid rgba(73, 72, 72, 0.791);
    display: block;
    padding: 0.5rem 0.5rem;
    border-radius: 10px;
    margin: 0.5rem;
    width: 20rem;
    transition: border-color 0.15s, box-shadow 0.15s;

}

input:focus, select:focus, textarea:focus {
    border-color: rgb(68, 171, 255);
    outline: 0;
    box-shadow: 0 0 0 4px rgb(176, 215, 245);
}
body {
  margin: 0;
}

</style>
