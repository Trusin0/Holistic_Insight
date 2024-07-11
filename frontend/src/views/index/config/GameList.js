export const gameList = [
  {
    id: 1,
    title: '反应时间',
    intro: '测试您的视觉反应',
    path: '/reaction-time',
    icon: require('@/assets/reaction-time-icon.png'),
    best: 1, // 最佳成绩取最大值/最小值，1 取最小值，-1取最大值
    section: 25, // 取值区块间隔
    scoreRange: [100, 500], // 成绩取值范围
    unit: 'ms'
  },
  {
    id: 2,
    title: '数字记忆',
    intro: '测试您的数字记忆能力',
    path: '/number-memory',
    icon: require('@/assets/number-memory-icon.png')
  },
  {
    id: 3,
    title: '舒尔特方格',
    intro: '随时随地打开，开启专注力训练',
    icon: require('@/assets/shuerte-grip-icon.png'),
    path: '/shuerte-grip'
  },
  {
    id: 4,
    title: '图形记忆',
    intro: '测试您的图形方格记忆能力',
    icon: require('@/assets/figure-memory-icon.png'),
    path: '/figure-memory'
  },
  {
    id: 5,
    title: 'MBTI人格测试',
    intro: '测试您的人格特质',
    icon: require('@/assets/MBTI-icon.png'),
    path: '/mbti'
  },
  {
    id: 6,
    title: '瞄准测试',
    intro: '测试您的鼠标定位能力',
    icon: require('@/assets/aim-test-icon.png'),
    path: '/aim-test'
  },
  {
    id: 7,
    title: '色觉敏感度测试',
    intro: '测试您的色觉敏感度',
    icon: require('@/assets/color-sensitivity-icon.png'),
    path: '/color-sensitivity'
  },
]
