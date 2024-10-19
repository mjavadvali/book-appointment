<template>
  <BaseAuthCard>
    <template #header>
      <base-auth-button :mode="loginButtonMode" @click="changeComponent('login')">Sign in</base-auth-button>
      <base-auth-button :mode="signupButtonMode" @click="changeComponent('sign-up')">Create account</base-auth-button>

    </template>
    <template #default>
      <component :is="displayingComponent"></component>
    </template>
    

  </BaseAuthCard>
</template>

<script>
import Login from './Login.vue'
import SignUp from './SignUp.vue'
import BaseAuthCard from '../UI/BaseAuthCard.vue';
import BaseButton from '../UI/BaseButton.vue';
export default {
  components: {
    Login,
    BaseAuthCard,
    BaseButton,
    SignUp
  },
  data() {
    return {
      displayingComponent: 'login'
    }
  },
  methods: {
    changeComponent(cmp) {
      
      this.displayingComponent = cmp
      console.log(this.displayingComponent);
    }
  },
  computed: {
    loginButtonMode() {
      return this.displayingComponent === 'login' ? 'flat' : null;
    },
    signupButtonMode() {
      return this.displayingComponent === 'sign-up' ? 'flat' : null;
    },
  }
}

</script>