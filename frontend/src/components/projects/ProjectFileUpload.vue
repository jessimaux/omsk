<template>
    <div class="row">
        <div class="col-lg-12">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Файлы</h5>
                    <div class="col-lg-4 mb-3">
                        <input multiple type="file" class="form-control" @input="inputFiles">
                    </div>
                    <div class="col-lg-6">
                        <ul class="list-group">
                            <li v-for="(file, index) in files" :key="index" class="list-group-item d-flex justify-content-between">
                                {{ file.name }}
                                <i class="bi bi-x-square" @click="deleteFile(index, files)"></i>
                            </li>
                            <li v-for="(file, index) in uploadedFiles" :key="index" class="list-group-item d-flex justify-content-between">
                                <a :href="file.file">{{ file.name }}</a>
                                <i class="bi bi-x-square" @click="deleteFile(index, uploadedFiles)"></i>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useProjectsStore } from '@/stores/projects'

export default {
    name: 'ProjectFileUpload',
    props: {
        files: {
            type: Object,
            required: true,
        },
        uploadedFiles: {
            type: Object,
            required: false,
        },
    },
    setup() {
        const projectsStore = useProjectsStore()
        return { projectsStore }
    },
    methods: {
        inputFiles(e) {
            for(let i = 0; i < e.target.files.length; i++) this.files.push(e.target.files[i])
        },
        
        deleteFile(index, fieldType) {
            fieldType.splice(index, 1)
        }
    },
}
</script>