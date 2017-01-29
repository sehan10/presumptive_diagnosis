   $(function () {
            Split =null;
            text ="";
            i=0;
            Parents = this.location.pathname;
            if(Parents.indexOf('Home')>0)
            {
                index =Parents.indexOf("Home");
               Split = index;
            }
             if(Parents.indexOf('AboutUs')>0)
            {
                index =Parents.indexOf("AboutUs");
                Split = index;
            }
             if(Parents.indexOf('ContactUs')>0)
            {
                index =Parents.indexOf('ContactUs');
               Split = index;
            }

             for( i=Split;i<Parents.length; i++)
             {
                 text = text+ Parents[i];

             }


           $('#'+ text).addClass('active');



        });