<script setup>
</script>

<template>
    <aside id="sidebar" class="sidebar">

        <ul class="sidebar-nav" id="sidebar-nav">

            <!-- <li class="nav-item">
                <router-link class="nav-link " :to="{ name: 'projects' }" active-class="active">
                    <i class="bi bi-grid"></i>
                    <span>Главная</span>
                </router-link>
            </li> -->

            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'projects' }" active-class="active"
                    :class="{ 'active': isActiveProjects }">
                    <i class="bi bi-grid"></i>
                    <span>Проекты</span>
                </router-link>
            </li>

            <li class="nav-item">
                <a class="nav-link collapsed" data-bs-target="#components-nav" data-bs-toggle="collapse" href="#">
                    <i class="bi bi-menu-button-wide"></i><span>Справочник</span>
                </a>
                <ul id="components-nav" class="nav-content collapse " data-bs-parent="#sidebar-nav">
                    <li>
                        <router-link :to="{ name: 'guide-products' }" active-class="active"
                            :class="{ 'active': isActiveProducts }">
                            <i class="bi bi-circle"></i><span>Товары</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-partners' }" active-class="active"
                            :class="{ 'active': isActivePartners }">
                            <i class="bi bi-circle"></i><span>Партнеры</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-providers' }" active-class="active"
                            :class="{ 'active': isActiveProviders }">
                            <i class="bi bi-circle"></i><span>Поставщики</span>
                        </router-link>
                    </li>

                    <li>
                        <router-link :to="{ name: 'guide-specifications' }" active-class="active"
                            :class="{ 'active': isActiveSpecifications }">
                            <i class="bi bi-circle"></i><span>Спецификации</span>
                        </router-link>
                    </li>
                </ul>
            </li>

            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'users' }" active-class="active"
                    :class="{ 'active': isActiveUsers }">
                    <i class=" bi bi-person"></i><span>Пользователи</span>
                </router-link>
            </li>

            <li class="nav-item">
                <router-link class="nav-link" :to="{ name: 'logs' }" active-class="active">
                    <i class="bi bi-file-earmark-text"></i><span>Логи действий</span>
                </router-link>
            </li>
        </ul>

    </aside>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "Sidebar",
    computed: {
        isActiveProducts() {
            return this.$route.name === 'guide-products-create' || this.$route.name === 'guide-products-edit'
        },
        isActiveProviders() {
            return this.$route.name === 'guide-providers-create' || this.$route.name === 'guide-providers-edit'
        },
        isActivePartners() {
            return this.$route.name === 'guide-partners-create' || this.$route.name === 'guide-partners-edit'
        },
        isActiveSpecifications() {
            return this.$route.name === 'guide-specifications-create' || this.$route.name === 'guide-specifications-edit'
        },
        isActiveProjects() {
            return this.$route.name === 'project-create' || this.$route.name === 'project-edit' || this.$route.name === 'project-purchase'
        },
        isActiveUsers() {
            return this.$route.name === 'user-create' || this.$route.name === 'user-edit'
        },
    }
})
</script>
