// electron.config.js for electron-builder

module.exports = {
  appId: 'com.example.myapp',
  productName: 'MyApp',
  win: {
    target: 'nsis',
    icon: 'build/icon.ico'
  },
  mac: {
    target: 'dmg',
    icon: 'build/icon.icns'
  },
  linux: {
    target: 'AppImage',
    icon: 'build/icon.png'
  },
  directories: {
    output: 'dist'
  }
};
