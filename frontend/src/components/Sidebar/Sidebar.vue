<script setup>
</script>

<template>
    <aside id="sidebar" class="sidebar">

        <ul class="sidebar-nav" id="sidebar-nav">

            <li class="nav-item">
                <router-link class="nav-link " :to="{ name: 'home' }" active-class="active">
                    <i class="bi bi-grid"></i>
                    <span>Главная</span>
                </router-link>
            </li><!-- End Dashboard Nav -->

            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'projects' }" active-class="active">
                    <i class="bi bi-grid"></i>
                    <span>Проекты</span>
                </router-link>
            </li>

            <li class="nav-item">
                <a class="nav-link collapsed" data-bs-target="#components-nav" data-bs-toggle="collapse" href="#">
                    <i class="bi bi-menu-button-wide"></i><span>Справочник</span><i
                        class="bi bi-chevron-down ms-auto"></i>
                </a>
                <ul id="components-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                    <li>
                        <router-link :to="{ name: 'guide-products' }" active-class="active">
                            <i class="bi bi-circle"></i><span>Товары</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-partners' }" active-class="active">
                            <i class="bi bi-circle"></i><span>Партнеры</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-providers' }" active-class="active">
                            <i class="bi bi-circle"></i><span>Поставщики</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-specifications' }" active-class="active">
                            <i class="bi bi-circle"></i><span>Спецификации</span>
                        </router-link>
                    </li>
                </ul>
            </li><!-- End Components Nav -->

        </ul>

    </aside><!-- End Sidebar-->
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "Sidebar",
});
</script>

<style scoped>

</style>
