<template>
  <div>
    <h2>Projects</h2>
    <ul>
      <li v-for="project in projects" :key="project.id">
        {{ project.project_name }}
      </li>
    </ul>
  </div>
</template>

<script>
import api from "../api";

export default {
  name: "Projects",
  data() {
    return {
      projects: [],
    };
  },
  created() {
    api.getProjects().then((response) => {
      this.projects = response.data;
    });
  },
};
</script>
