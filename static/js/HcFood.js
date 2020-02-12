Highcharts.chart('container', {
      chart: {
        type: 'line'
      },
      title: {
        text: ''
      },
      subtitle: {
        text: ''
      },
      xAxis: {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
      },
      yAxis: {
        title: {
          text: '배급량'
        }
      },
      plotOptions: {
        line: {
          dataLabels: {
            enabled: true
          },
          enableMouseTracking: true
        }
      },
      series: [{
        name: '사료(gram)',
        data: [
            janMf,
            febMf,
            marMf,
            aprMf,
            mayMf,
            junMf,
            julMf,
            augMf ]
      }, {
        name: '간식(갯수)',
        data: [
            janMs,
            febMs,
            marMs,
            aprMs,
            mayMs,
            junMs,
            julMs,
            augMs ]
      }]
    });