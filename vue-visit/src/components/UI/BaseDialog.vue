<template>
    
    <dialog open>
        <header>
            <slot name="header">
            </slot>
        </header>
        <main>
            <slot>
                
            </slot>
        </main>
        <button>
            <slot name="button">Okay</slot>
        </button>
    </dialog>
</template>


<script>


</script>


<style scoped>



header {
    position: absolute;
    top: 0; /* Stick it to the top */
    left: 0; /* Align to the left */
    right: 0;
    width: 100%;
    height: 3rem;
    border-radius: 25px 25px 0px 0;
    background: #0fd29d;
    border-bottom: 1px solid rgb(1, 92, 39);
}
dialog {
    top: -110vh;
    box-shadow: 1px 1px 7px 0px #479125;
    margin: auto;
    margin-top: 5rem;
    width: 40rem;
    height: 15rem;
    border: none;
    border-radius: 25px;
    position: relative;
}
p {
    margin-top: 5rem;
}

button {
    position: absolute;
    width: 5rem;
    background: #09d27c;
    height: 2rem;
    bottom: 20px;
    right: 25px;
    border-radius: 25px;
    border: 1px solid rgb(0, 128, 81);
    transition: transform 0.1s;

}

button:hover {
    transform: scale(1.05);
}

main {
    width: 35rem;
    height: 8rem;
    margin: auto;
    margin-top: 6.5rem;
}

</style>