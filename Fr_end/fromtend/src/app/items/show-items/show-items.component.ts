import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';


@Component({
  selector: 'app-show-items',
  templateUrl: './show-items.component.html',
  styleUrls: ['./show-items.component.css']
})



export class ShowItemsComponent implements OnInit {
  static addClick: any;

  constructor(private service:SharedService) { }

  ItemList:any=[];

  ModalTitle!: string;
  ActivateAddEditItemsComp:boolean=false;
  item:any;

  ngOnInit(): void {
    this.refreshitemList();
  }


  
  addClick(){
    this.item={
      id:"",
      ItenName:"",
      ItemCode:"",
      SKU:"",
      ReferralCode:""
    }
     
    this.ModalTitle="Add Item";
    this.ActivateAddEditItemsComp=true;
    this.refreshitemList();

  }

  editClick(item: any){
    console.log(item);
    this.item=item;
    this.ModalTitle="Edit Item";
    this.ActivateAddEditItemsComp=true;
    this.refreshitemList();
  }

  deleteClick(item: {id: number}){

    if(confirm('Are you sure??')){
      console.log(item)
      this.service.deleteitems(item.id).subscribe((data: any)=>{
        this.refreshitemList();
      })
    }
  }

  closeClick(){
    this.ActivateAddEditItemsComp=false;
    this.refreshitemList();
  }
  

  refreshitemList(){
    this.service.getitemsList().subscribe((data: any)=>{
      // this.ActivateAddEditItemsComp=false;
      this.ItemList=data;
    });
  }

}