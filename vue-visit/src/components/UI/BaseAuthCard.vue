<template>
    <div class="signin">
        <header>
            <slot name="header"></slot>
        </header>
        <form>
            <main>
                <slot></slot>
            </main>
            <footer>
                <slot name="btns"></slot>
            </footer>
        </form>
    </div>
</template>

<style scoped>
.signin form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 1.75rem;
}

.signin {
    border: 1px solid rgb(121, 241, 185);
    border-radius: 9px;
    width: 28rem;
    height: 23rem;
    background: rgb(241, 243, 242);
    margin: auto;
    margin-top: 8rem;
}

.signin a {
    font-size: 14px;
    text-decoration: none;
}

header {
    display: flex;
    gap: 3rem;
    height: 3rem;
    background: #638871;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-items: stretch;
    align-content: space-around;
    padding-left: 3rem;
    padding-right: 3rem;
}
</style>