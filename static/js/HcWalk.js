Highcharts.chart('container4', {
      chart: {
        zoomType: 'xy'
      },
      title: {
        text: ''
      },
      subtitle: {
        text: ''
      },
      xAxis: [{
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
        crosshair: true
      }],
      yAxis: [{ // Primary yAxis
        labels: {
          format: '{value} 회',
          style: {
            color: Highcharts.getOptions().colors[1]
          }
        },
        title: {
          text: '전체평균',
          style: {
            color: Highcharts.getOptions().colors[1]
          }
        }
      }, { // Secondary yAxis
        title: {
          text: '내 평균',
          style: {
            color: Highcharts.getOptions().colors[0]
          }
        },
        labels: {
          format: '{value} 회',
          style: {
            color: Highcharts.getOptions().colors[0]
          }
        },
        opposite: true
      }],
      tooltip: {
        shared: true
      },
      legend: {
        layout: 'vertical',
        align: 'left',
        x: 120,
        verticalAlign: 'top',
        y: 100,
        floating: true,
        backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255,255,255,0.25)'
      },
      series: [{
        name: '내 평균',
        type: 'column',
        yAxis: 1,
        data: [
            janMw,
            febMw,
            marMw,
            aprMw,
            mayMw,
            junMw,
            julMw,
            augMw ],
        tooltip: {
          valueSuffix: ' 회'
        }

      }, {
        name: '전체평균',
        type: 'spline',
        yAxis: 1,
        data: [
            janMwa,
            febMwa,
            marMwa,
            aprMwa,
            mayMwa,
            junMwa,
            julMwa,
            augMwa ],
        tooltip: {
          valueSuffix: ' 회'
        }
      }]
    });