<template>
  <form @submit.prevent="submitDefect">
    <input v-model="summary" placeholder="Defect Summary" required />
    <select v-model="priority">
      <option>Low</option>
      <option>Medium</option>
      <option>High</option>
    </select>
    <button type="submit">Add Defect</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      summary: '',
      priority: 'Low',
    };
  },
  methods: {
    async submitDefect() {
      await this.$axios.post(`/api/projects/${this.projectId}/defects`, {
        summary: this.summary,
        priority: this.priority,
      });
      this.$emit('refresh');
    },
  },
};
</script>