<template>
    <div>

        <h2>You have logged out</h2>
        <h3>click 
            <router-link to="/user_auth">
                here
            </router-link>
           
             to sign in</h3>
    </div>
</template>


<style scoped>

div {
    display: flex;
    margin-top: 10rem;
    flex-direction: column;
    align-content: stretch;
    justify-content: space-around;
    align-items: center;
    flex-wrap: nowrap;
}

</style>