<template>
    <div>
        <el-collapse
            v-model="activeName"
            accordion
        >
            <el-collapse-item
                title="归档信息"
                name="1"
            >
                <div>2018</div>
                <div>2017</div>
                </el-collapse-item>
                <el-collapse-item
                    title="技术分类"
                    name="2"
                >
                    <div>JavaScript</div>
                    <div>Python</div>
                    </el-collapse-item>
                    <el-collapse-item
                        title="最热文章"
                        name="3"
                    >
                        <div>简化流程：设计简洁直观的操作流程；</div>
                        <div>清晰明确：语言表达清晰且表意明确，让用户快速理解进而作出决策；</div>
                        <div>帮助用户识别：界面简单直白，让用户快速识别而非回忆，减少用户记忆负担。</div>
                        </el-collapse-item>
                        <el-collapse-item
                            title="可控 Controllability"
                            name="4"
                        >
                            <div>用户决策：根据场景可给予用户操作建议或安全提示，但不能代替用户进行决策；</div>
                            <div>结果可控：用户可以自由的进行操作，包括撤销、回退和终止当前操作等。</div>
                            </el-collapse-item>
                            </el-collapse>
    </div>
</template>

//
<script>
export default {
    data() {
      return {
        activeName: '1'
      };
    }
}
</script>

//
<style scoped>

</style>
