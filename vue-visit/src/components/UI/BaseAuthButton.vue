<template>
    <button :class="mode">
        <slot></slot>
    </button>
</template>

<script>
export default {
    props: ['mode']
}
</script>

<style scoped>
button {
    background: #03b985;
    width: 7rem;
    border: none;
    margin-left: -3rem;
    border: 1px solid black;
    transition: transform 0.2s;
}
button:hover {
    transform: scale(1.01);
}
.flat {
    /* background: rgb(59, 100, 136); */
    /* filter: blur(0.8px); */
    /* background: #5dbea2; */
    border: rgb(200, 255, 0) 2px solid;
    
}

.flat:focus {
}
</style>