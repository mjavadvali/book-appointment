<template>
    <div>
        <header>
            <slot name="header">
                <section class="image"></section>
            </slot>
        </header>
        <main>
            <slot></slot>
        </main>
        <footer>
            <slot name="footer"></slot>
        </footer>
    </div>
</template>


<style scoped>


div {
    
    width: 20rem;
    height: 20rem;
    margin-left: 1rem;
    border-radius: 10px;
    box-shadow: 0px 0px 11px 0px #9b9696;
    position: relative;
    margin: autos;
    /* display: flex; */
    transition: transform 0.2s;
}

div:hover {
 transform: scale(1.03);
}

section {
    width: 100%;
    height: 10rem;
    border: 1px solid blue;
}

main {
    margin-left: 6px;
}

footer {
    position: absolute;
    bottom: 0;
    margin-bottom: 5px;
    margin-left: 6px
}


header {
    text-align-last: center;
    border-bottom: 1px solid #c9c0c0;
}
</style>