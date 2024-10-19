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
    background: rgb(14, 210, 119);
    border: 0cap;
    padding: 0.5rem 1rem;
    border-radius: 5px;
    margin: auto 0;
    transition: transform 0.15s;
}
button:hover {
    transform: scale(1.06);
    background: rgb(118, 151, 128);
}
.flat {
    background: aliceblue;
    border: 1px solid #09d009;
}

.alert {
    background: rgb(226, 92, 135);
}

button .header {
    height: 100%;
    width: 6rem;
}
.profile {
    height: 100%;
    border-radius: 1px;
    border-left: 1px solid rgb(56, 90, 70);
}
</style>