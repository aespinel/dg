define([
  'jquery',
  'underscore',
  'backbone',
  'configs',
  'indexeddb_backbone_config',
  'configs',
  
], function($,pass, pass, configs, indexeddb, all_configs){
    
    var DashboardView = Backbone.Layout.extend({
      template: "#dashboard",
      events: {
          "click button#download": "Download",
          "click button#upload": "Upload"
      },
      item_template: _.template($("#dashboard_item_template").html()),
      
      initialize: function(){
          
          // add dummy data to uploadqueue
          var generic_model_offline = Backbone.Model.extend({
                database: indexeddb,
                storeName: "uploadqueue",
          });
            
          var generic_offline_collection = Backbone.Collection.extend({
              model: generic_model_offline,
              database: indexeddb,
              storeName: "uploadqueue",
          });
          var dummy_data_collection = new generic_offline_collection();
          
          var generic_model_offline2 = Backbone.Model.extend({
                database: indexeddb,
                storeName: "person",
          });
          var generic_model_offline_vill = Backbone.Model.extend({
                database: indexeddb,
                storeName: "village",
          });
          // var rem_model = new generic_model_offline();
          // rem_model.set({id:"76e162e5-958b-0df5-b414-4b7a8b4f948b"});
          // rem_model.destroy();
          
          // create a village, create a person in that village, edit the person and delete it
          var dummy_person = new generic_model_offline2();
          var dummy_vill = new generic_model_offline_vill();
          dummy_vill.set({village_name:"dummy_village_here",online_id:10000000000251});
          dummy_vill.save(null,{
              success: function(model)
              {
                  console.log("UPLOAD: Dummy offline village model after add save - "+ JSON.stringify(model.toJSON()));
                  dummy_person.set({age: 23,father_name: "asd",gender: "M",person_name: "sdk",village: model.id});
                  console.log("UPLOAD: Dummy offline person model before save - "+ JSON.stringify(dummy_person.toJSON()));
                  dummy_person.save(null,{
                      success:function(model)
                      {          
                          console.log("UPLOAD: Dummy offline person model after add save - "+ JSON.stringify(model.toJSON()));
                          console.log("UPLOAD: Adding a model to uploadqueue");
                          dummy_data_collection.create({data:model.toJSON(),action:"A",entity_name:"person"},
                                            {
                                                success:function(model)
                                                {          
                                                    console.log("UPLOAD: Added a model to uploadqueue - "+ JSON.stringify(model.toJSON()));
                                            
                                                }
                                            }
                          );
                          model.set('age',24);
                          console.log("UPLOAD: Dummy offline person model before edit save - "+ JSON.stringify(model.toJSON()));
                          model.save(null,{
                              success:function(model)
                              {          
                                  console.log("UPLOAD: Dummy offline person model after edit save - "+ JSON.stringify(model.toJSON()));
                                  console.log("UPLOAD: Adding a model to uploadqueue");
                                  dummy_data_collection.create({data:model.toJSON(),action:"E",entity_name:"person"},
                                  {
                                      success:function(model)
                                      {          
                                          console.log("UPLOAD: Added a model to uploadqueue - "+ JSON.stringify(model.toJSON()));
                                            
                                      }
                                  }
                              );
                              // delete the model
                                  // model.destroy({
//                                       success: function(model_d){
//                                           console.log("UPLOAD: Deleted model.");
//                                           console.log("UPLOAD: Deleted an offline model - "+ JSON.stringify(model_d.toJSON()));
//                                           dummy_data_collection.create({data:model_d.toJSON(),action:"D",entity_name:"person"},
//                                           {
//                                               success:function(model)
//                                               {          
//                                                   console.log("UPLOAD: Added a model to uploadqueue - "+ JSON.stringify(model.toJSON()));
//                                             
//                                               }
//                                           }
//                                       );
//                           
//                                   
//                                       },
//                                       error: function(){
//                                           console.log("UPLOAD: Error deleting model.")
//                                       }
//                                   });
          
                              }
                          });
          
                      }
                  });
                      
                     
              },
              error: function()
              {
                  console.log("UPLOAD: Error creating a dummy village.")
              }
          });


          /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
          /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
      },
      
      Upload: function(){
          console.log("UPLOAD: start the fuckin upload");
          
          // fetch the upload queue from indexeddb
          var generic_model_offline = Backbone.Model.extend({
                database: indexeddb,
                storeName: "uploadqueue",
          });
          var generic_offline_collection = Backbone.Collection.extend({
              model: generic_model_offline,
              database: indexeddb,
              storeName: "uploadqueue",
          });
          this.upload_collection = new generic_offline_collection();
          this.upload_collection.bind('reset', this.process_upload_queue, this);
          this.upload_collection.fetch();
          ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
      },
      
      // read each entry of the uploadqueue 
      process_upload_queue: function(){
          console.log("UPLOAD: inside upload queue: "+this.upload_collection.length+" entries");
          console.log((this.upload_collection.models));
          $(document).on("read_next",this.next_upload);
          ev = {
          	type: "read_next",
          	context: this
          };
          $.event.trigger(ev);
          this.upload_collection.each(function(model) {
             // this.process_upload_entry(model);
             // model.destroy();
            }, this);
            
        
            
      },
     ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
     
     next_upload: function(event){
         event.stopPropagation();
       
         console.log("in next_upload"); 
       var model1 = event.context.upload_collection.shift();
       if(model1==undefined)
       return;
       console.log(model1);
          
       event.context.process_upload_entry(model1);
       
     },
      
      process_upload_entry: function(entry){
          console.log("UPLOAD: processing this uploadqueue entry - "+ JSON.stringify(entry.toJSON()));
          
          if(entry.get("action") == "A"||entry.get("action") == "E")
          {
              console.log("UPLOAD: its add or edit action");
              this.offline_to_online(entry);
          }
          else if(entry.get("action") == "D")
          {
              console.log("UPLOAD: its delete action");
              this.upload_delete(entry);
          }
          else
          {
              console.log("ERROR:UPLOAD: its ambigous action in entry. None of A,E,D");
              alert("ERROR!");
              
          }
          
            
            
          
      },
      
      offline_to_online: function(entry){
          console.log("UPLOAD:OFFLINE_TO_ONLINE: here am i");
          var f_entities = all_configs[entry.get('entity_name')]["foreign_entities"];
          console.log("UPLOAD:OFFLINE_TO_ONLINE: foreign entities for the model under consideration"+JSON.stringify(f_entities));
          // var online_json = jQuery.extend(true, {}, entry.get("data"));
          var online_json = entry.get("data");
          console.log("UPLOAD:OFFLINE_TO_ONLINE: json before converting"+JSON.stringify(entry.get("data")));
          var num_mem = f_entities.length;
          for (member in f_entities)
          {
              if(!(member in entry.get("data")))
                  continue;
              console.log("UPLOAD:OFFLINE_TO_ONLINE: converting "+member+" offline to online");
              var generic_model_offline = Backbone.Model.extend({
                    database: indexeddb,
                    storeName: member,
              });
              var f_model = new generic_model_offline();
              f_model.set("id", entry.get("data")[member]);
              var that = this;
              f_model.fetch({
                  success: function(model){
                      console.log("UPLOAD:OFFLINE_TO_ONLINE: The foreign entity with the key mentioned fetched from IDB- "+JSON.stringify(model.toJSON()));
                      console.log("UPLOAD:OFFLINE_TO_ONLINE: member"+member);
                      console.log("UPLOAD:OFFLINE_TO_ONLINE: but"+ model.storeName);
                      online_json[model.storeName] = all_configs[entry.get('entity_name')]["rest_api_url"] + model.get("online_id")+"/";
                      console.log("UPLOAD:OFFLINE_TO_ONLINE: json after converting"+JSON.stringify(online_json));
                      num_mem--;
                      if(!num_mem)
                          {
                              console.log("UPLOAD:OFFLINE_TO_ONLINE: all converted");
                              if(entry.get("action") == "A")
                              {
                                  console.log("UPLOAD: its add action");
                                  that.upload_add(entry);
                              }
                              else if(entry.get("action") == "E")
                              {
                                  console.log("UPLOAD: its edit action");
                                  that.upload_edit(entry);
                              }
          
                          }
                  },
                  error: function(){
                      console.log("UPLOAD:OFFLINE_TO_ONLINE: The foreign entity with the key mentioned does not exist anymore.");
                      //TODO: discard this and continue with next uploadqueue entry
                  }
              });
          }
          
          
            
      },
      
      upload_add: function(entry){
          
          // create online,offline models for the entity of upload entry
            var generic_model_online = Backbone.Model.extend({
                sync: Backbone.ajaxSync,
                url: function() {
                    return this.id ? all_configs[entry.get("entity_name")].rest_api_url + this.id + "/" : all_configs[entry.get("entity_name")].rest_api_url;
                },
            });
            var generic_model_offline = Backbone.Model.extend({
                  database: indexeddb,
                  storeName: entry.get("entity_name"),
            });
          
            var upload_online_model = new generic_model_online();
            var upload_offline_model = new generic_model_offline();
         ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        // set json from uploadqueue entry on online model, unset the id, save the model     
            var offline_id = entry.get("data").id;
            
            upload_offline_model.set("id",offline_id);
            var that = this;      
            var fetching = upload_offline_model.fetch({
                success:function(model)
                {   // not deleted hence go forward
                    
                    // var online_json = that.offline_to_online(entry);      
                    upload_online_model.set(entry.get("data"));    //setting what was recorded and not the exact model
                    upload_online_model.unset('id');
                    console.log("UPLOAD:ADD: upload online model set - "+JSON.stringify(upload_online_model.toJSON()));
                    console.log("UPLOAD:ADD: upload online model save called.");
                    upload_online_model.save(null,{
                          async:false,
                          success:function(online_model)
                          {          
                              console.log("UPLOAD:ADD: Dummy online person model after save - "+ JSON.stringify(upload_online_model.toJSON()));
                  
                              // set online id in offline model
                                      model.set('online_id',upload_online_model.get("id"));
                                      model.save(null,{
                                          success: function(model)
                                          {          
                                              console.log("UPLOAD:ADD: offline model after evrthing-" + JSON.stringify(model.toJSON()));
                                              entry.destroy();
                                              $.event.trigger(ev);
                                          },
                                          error: function() {
                                              //ToDO: error handling
                                              console.log("ERROR:UPLOAD:ADD: The offline model's online id could not be set.");
                                              entry.destroy();
                                              $.event.trigger(ev);
                                              
                                          }
                                    });
                            },
                            error: function()
                            {
                                console.log("UPLOAD:ADD: Error adding model on server ");
                                entry.destroy();
                                $.event.trigger(ev);
                            }
                      });
                  
                          ///////////////////////////////////////////////////////////////////////////////////////////////////
                       
            
                },
                error: function() {
                    console.log("ERROR:UPLOAD:ADD: The offline model does not exist in indexeddb anymore. Can't set its online id. Must be deleted. Ignoring. ");
                    entry.destroy();
                    $.event.trigger(ev);
                }
              });

          
      },
      
      upload_edit: function(entry){
          // create online,offline models for the entity of upload entry
            var generic_model_online = Backbone.Model.extend({
                sync: Backbone.ajaxSync,
                url: function() {
                    return this.id ? all_configs[entry.get("entity_name")].rest_api_url + this.id + "/" : all_configs[entry.get("entity_name")].rest_api_url;
                },
            });
            var generic_model_offline = Backbone.Model.extend({
                  database: indexeddb,
                  storeName: entry.get("entity_name"),
            });
          
            var upload_offline_model = new generic_model_offline();
            var upload_online_model = new generic_model_online();
         ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        // set json from uploadqueue entry on online model, unset the id, save the model     
            upload_offline_model.set(entry.get("data"));
            var fetching = upload_offline_model.fetch({
                success:function(model)
                {          
                    console.log("UPLOAD:EDIT: offline model fetched to get online id-" + JSON.stringify(model.toJSON()));
                    upload_online_model.set(entry.get("data"));
                    console.log("UPLOAD:EDIT: upload online model from uploadqueue- "+JSON.stringify(upload_online_model.toJSON()));
                    upload_online_model.set('id',model.get('online_id'));
                    upload_online_model.unset('online_id');
                    console.log("UPLOAD:EDIT: upload online model set - "+JSON.stringify(upload_online_model.toJSON()));
                    upload_online_model.save(null,{
                      success:function(model)
                      {          
                          console.log("UPLOAD:EDIT: Dummy online person model after save - "+ JSON.stringify(upload_online_model.toJSON()));
                          entry.destroy();
                          $.event.trigger(ev);
                      },
                      error:function(model)
                      {
                          console.log("UPLOAD:EDIT: Erro editing model on server ");
                          entry.destroy();    
                          $.event.trigger(ev);
                      }
                    });
                    console.log("UPLOAD:EDIT: upload online model save called.");
                    
                },
                error: function() {
                    //ToDO: error handling
                    console.log("ERROR:UPLOAD:EDIT: The offline model does not exist in indexeddb. Can't get its online id. Ignoring. ");
                    entry.destroy();
                    $.event.trigger(ev);
                }
              });
            
       /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
          
      },
      
      upload_delete: function(entry){
          // create online,offline models for the entity of upload entry
          var generic_model_online = Backbone.Model.extend({
              sync: Backbone.ajaxSync,
              url: function() {
                  return this.id ? all_configs[entry.get("entity_name")].rest_api_url + this.id + "/" : all_configs[entry.get("entity_name")].rest_api_url;
              },
          });
          var generic_model_offline = Backbone.Model.extend({
                database: indexeddb,
                storeName: entry.get("entity_name"),
          });
          
          var upload_offline_model = new generic_model_offline();
          var upload_online_model = new generic_model_online();
       ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
      // 
          if ('online_id' in entry.get("data"))
          {
              upload_online_model.set(entry.get("data"));
              console.log("UPLOAD:DELETE: upload online model from uploadqueue- "+JSON.stringify(upload_online_model.toJSON()));
              upload_online_model.set('id',upload_online_model.get('online_id'));
              upload_online_model.unset('online_id');
              console.log("UPLOAD:DELETE: upload online model set - "+JSON.stringify(upload_online_model.toJSON()));
              upload_online_model.delete(null,{
                success:function(model)
                {          
                    console.log("UPLOAD:DELETE: deleted ");
                    entry.destroy();
                    $.event.trigger(ev);
                },
                error: function(){
                    console.log("UPLOAD:DELETE: Error while deleting on server ");
                    entry.destroy();          
                    $.event.trigger(ev);
                    
                }
              });
              console.log("UPLOAD:DELETE: upload online model delete called.");
          }
          else
          {
              console.log("UPLOAD:DELETE: No online_id was found on the model when deleted. Therefore its not on server yet. Hence taking no action.");
              entry.destroy();
              $.event.trigger(ev);
              
          }
     /////////////////////////////////////////////////////////////////////////////////////////////////////////////////
          
    
            
          
      },
      
      afterRender: function() {
          /* Work with the View after render. */
          // this.collection.fetch();
          for (var member in configs) {
              // console.log(configs[member]);
              $('tbody').append(this.item_template({name: member,title: configs[member]["page_header"]}));
              
            }
      },
      
      fetch_save: function(config) {
          var prevTime, curTime;
          curTime = (new Date())
              .getTime();
          prevTime = curTime;
          console.log("DASHBOARD:DOWNLOAD: downloading  " + config.page_header);
          var generic_model_offline = Backbone.Model.extend({
                database: indexeddb,
                storeName: config.entity_name,
          });
          
          var generic_collection_offline = Backbone.Collection.extend({
                model: generic_model_offline,
                database: indexeddb,
                storeName: config.entity_name,
          });
          
          var generic_collection_online = Backbone.Collection.extend({
                url: config.rest_api_url,
                sync: Backbone.ajaxSync,
                parse: function(data) {
                    return data.objects;
                }

          });
            
          var collection_offline = new generic_collection_offline();
          var collection_online = new generic_collection_online(); 
          console.log(collection_offline);
          console.log(collection_online);
          
          collection_online.fetch({
              data: { limit: 100},
              success: function() {
                  data = (collection_online.toJSON());
                  console.log("DASHBOARD:DOWNLOAD: "+config.entity_name + " collection fetched ");
                  curTime = (new Date())
                      .getTime();
                  deltaTime = curTime - prevTime;
                  var download_time = deltaTime;
                  prevTime = curTime;
                  var db;
                  var request = indexedDB.open("coco-database");
                  request.onerror = function(event) {
                      console.log("DASHBOARD:DOWNLOAD: "+"Why didn't you allow my web app to use IndexedDB?!");
                  };
                  request.onsuccess = function(event) {
                      db = request.result;
                      var clearTransaction = db.transaction([config.entity_name], "readwrite");
                      var clearRequest = clearTransaction.objectStore(config.entity_name)
                          .clear();
                      clearRequest.onsuccess = function(event) {
                          console.log("DASHBOARD:DOWNLOAD: "+config.entity_name + ' objectstore cleared');
                          console.log(collection_offline);
          
                          for (var i = 0; i < data.length; i++) {
                              // console.log(data[i]);
                              // adding online_id field to support offline functionality
                              data[i]['online_id'] = data[i]['id'];
                              collection_offline.create(data[i]);
                          }
    
                          curTime = (new Date())
                              .getTime();
    
                          deltaTime = curTime - prevTime;
                          var writing_time = deltaTime;
                          console.log("DASHBOARD:DOWNLOAD: "+config.entity_name + " downloaded");
                          console.log("DASHBOARD:DOWNLOAD: "+config.entity_name + " downlaod time = " + download_time);
                          console.log("DASHBOARD:DOWNLOAD: "+config.entity_name + " writing time = " + writing_time);
    
                      };
    
    
    
                  }
              }
          });
      },
      Download: function() {
          console.log("starting download");
          //Download:fetch each model from server and save it to the indexeddb
    
    
          for (var member in configs) {
              // console.log(configs[member]);
              this.fetch_save(configs[member]);
         
            }
            
      },
        
    });
    
    
  // Our module now returns our view
  return DashboardView;
});