from skill_system import skill_deployer

skill01 = skill_deployer.SKillDeployer("降龙十八掌")
skill01.deploy_skill()
from skill_system.skill_deployer import SKillDeployer
skill02 =SKillDeployer("天下无狗")
skill02.deploy_skill()


from day20.common import StudentManagerView

view =StudentManagerView()
view.main()

view = double_list_helper.StudentManagerView()
view.main()