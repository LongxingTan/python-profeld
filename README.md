# Survival_analysis
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg)](https://github.com/996icu/996.ICU/blob/master/LICENSE)<br>
This repository is to briefly introduce how to implement survival analysis and predictive maintenance in python. 

> ### Ongoing project, welcome to join, I'm too lazy.

## Why this repository?
Survival analysis, is an important area for me. This is where my career started, after graduation I joined Mercedes-Benz and worked as a pioneer to improve the field quality with data. It's still a dream time to work together with Dr. Andreas Jacobi and [Christoph Jordan](https://www.linkedin.com/in/christoph-jordan-905649157/) to predict the vehicle's future performance in quality, and we really made a difference and helped a lot for Mercedes customers to have a better product. (Even so, I still cannot afford one, just like thousand years ago Chinese poet said: 遍身罗绮者，不是养蚕人)

After that, I focus more on programming and machine learning step by step, slowly but continuously. Now I have left Mercedes, Bolin and Kim will continue to support on this. And I joined a startup Teletraan as a data scientist, I also implement predictive maintenance methods for industry. Cheers for the great time! It's time to have an overview about this topic and add some new things I learned recently.

Please note that this repository only includes my own understanding of survival analysis and does not leak any confidential information.
I will consider this as a witness of the pleasant time we spent together.

## Introduction

----
### Preventive maintenance/ Survival analysis
Preventive maintenance consider all samples ststistical property, instead of each member's, we can decide to maintain or not when the operation time reaches the mean time. Survival analysis do the similar thing, but it can also predict the whole samples's future performance. So that's why we use survival analysis in Mercedes, to evaluate vehicle issue's future performance. 


<table style="width:100%" align="center">
  <tr>
    <th>
      <p align="center">
      Weibull                      
      </p>
    </th>
    <th>
      <p align="center">
           <a href="./examples/weibull_tutorial.ipynb" name="introduction">intro & examples</a>             
      </p>
     </th>
    <th>
       <p align="center">           
           <a href="./src/weibull/weibull.py" name="code">core code</a>     
      </p>
    </th> 
  </tr>
  <tr>
    <th>
      <p align="center">
      WTTE-RNN                     
      </p>
    </th>
    <th>
      <p align="center">
           <a href="./docs/arima.md" name="introduction">intro & examples</a>             
      </p>
     </th>
    <th>
       <p align="center">           
           <a href="./deepts/models/arima.py" name="code">core code</a>     
      </p>
    </th> 
  </tr>    
  <tr>
    <th>
      <p align="center"> Local weighted Weibull                      
      </p>
    </th>
    <th>
      <p align="center">
           <a href="./docs/arima.md" name="introduction">intro & examples</a>             
      </p>
     </th>
    <th>
       <p align="center">           
           <a href="./deepts/models/arima.py" name="code">core code</a>     
      </p>
    </th> 
  </tr>
</table>

Further: Segmented regression, isotonic regression
---
### Predictive maintenance
predcitive maintenance predict a specific member's future performance giving its historical feature data. It encompasses a variety of topics, including but not limited to: failure prediction, failure diagnosis (root cause analysis), failure detection, failure type classification, and recommendation of mitigation or maintenance actions after failure. It's helpful to reduce repair costs, reduce production down time and improve worker safety.

Predictive maintenance differs from preventive maintenance because it relies on the actual condition of equipment, rather than average or expected life statistics, to predict when maintenance will be required, so predictive maintenance gives personal prediction service.


<table style="width:100%" align="center">  
  <tr>
    <th>
      <p align="center">
      Remaining useful life                      
      </p>
    </th>
    <th>
      <p align="center">
           <a href="./docs/arima.md" name="introduction">intro & examples</a>             
      </p>
     </th>
    <th>
       <p align="center">           
           <a href="./deepts/models/arima.py" name="code">core code</a>     
      </p>
    </th> 
  </tr>
  <tr>
    <th>
      <p align="center">
      Classification                      
      </p>
    </th>
    <th>
      <p align="center">
           <a href="./docs/arima.md" name="introduction">intro & examples</a>             
      </p>
     </th>
    <th>
       <p align="center">           
           <a href="./deepts/models/arima.py" name="code">core code</a>     
      </p>
    </th> 
  </tr>

</table>

------
## Further reading
- [prediction-of-battery-cycle-life](https://github.com/rdbraatz/data-driven-prediction-of-battery-cycle-life-before-capacity-degradation)
- [long-live-the-battery](https://github.com/dsr-18/long-live-the-battery),  [intro](https://towardsdatascience.com/predicting-battery-lifetime-with-cnns-c5e1faeecc8f)
- [Battery-life-estimation](https://github.com/zhouxf53/Battery-life-estimation)
- [LSTM Predictive-Maintenance](https://github.com/umbertogriffo/Predictive-Maintenance-using-LSTM)
- [Azure_Predictive-Maintenance](https://gallery.azure.ai/Collection/Predictive-Maintenance-Template-3)
- [AWS_predictive-maintenance](https://github.com/awslabs/predictive-maintenance-using-machine-learning)
- [lifelines](https://github.com/CamDavidsonPilon/lifelines)
- [machine-learning-techniques-predictive-maintenance](https://www.infoq.com/articles/machine-learning-techniques-predictive-maintenance/)
- [Mathworks-predictive-maintenance](https://www.mathworks.com/solutions/predictive-maintenance.html)
- [intelligent fault diagnosis and remaining useful life prediction of rotating machinery](https://books.google.com.hk/books?id=fTJQDAAAQBAJ&printsec=frontcover#v=onepage&q&f=false))

#### If you are interested in more Data Science applications in Automotive Industry, follow my friend YueTan's WeChat account if you are so luckily to know Chinese. 
Any equations, feel free to open an issue or follow the WeChat.


<img src="./docs/assets/public_account.jpg" height="200">
<!-- 
[comment]: <img src="./docs/assets/knowledge.png" height="200">
<img src="./docs/assets/live_long.jpg" height="200"> -->
