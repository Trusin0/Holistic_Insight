export const gameList = [
  {
    id: 1,
    title: '反应时间',
    intro: '测试您的视觉反应',
    path: '/reaction-time',
    best: 1, // 最佳成绩取最大值/最小值，1 取最小值，-1取最大值
    section: 25, // 取值区块间隔
    scoreRange: [100, 500], // 成绩取值范围
    unit: 'ms'
  },
  {
    id: 2,
    title: '数字记忆',
    intro: '测试您的数字记忆能力',
    path: '/number-memory'
  },
  {
    id: 3,
    title: '舒尔特方格',
    intro: '随时随地打开，开启专注力训练',
    path: '/shuerte-grip'
  },
  {
    id: 4,
    title: '图形记忆',
    intro: '测试您的图形方格记忆能力',
    path: '/figure-memory'
  },
  {
    id: 5,
    title: 'MBTI人格测试',
    intro: '测试您的人格特质',
    path: '/mbti'
  },
  {
    id: 6,
    title: '瞄准测试',
    intro: '测试您的鼠标定位能力',
    path: '/aim-test'
  }
]
