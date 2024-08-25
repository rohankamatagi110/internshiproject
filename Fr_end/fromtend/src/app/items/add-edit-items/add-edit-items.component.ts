import { Component, OnInit,Input } from '@angular/core';
import {SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-add-edit-items',
  templateUrl: './add-edit-items.component.html',
  styleUrls: ['./add-edit-items.component.css']
})
export class AddEditItemsComponent implements OnInit {

  constructor(private service:SharedService) { }
 

  @Input() item:any;
  @Input() formMode:any;
  id: number = 1;
  // Sno: number = 0;
  ItemName: string = '';
  ItemCode: string = '';
  SKU: string = '';
  ReferralCode: string = '';

  ngOnInit(): void {
    console.log("selectedItem", this.item);
    this.id = this.item.id;
    this.ItemName = this.item.ItemName;
    this.ItemCode = this.item.ItemCode;
    this.SKU = this.item.SKU;
    this.ReferralCode = this.item.ReferalCode;
  }  

  itemList:any=[];

  additem(){

    var val = {id:this.id,
              ItemName:this.ItemName,
              ItemCode:this.ItemCode,
              SKU:this.SKU,
              ReferralCode:"w"};
    console.log("Adding Item")
    console.log(val)

    this.service.additems(val).subscribe((res: { toString: () => any; })=>{
      // alert(res.toString());
      // if ( "message"  "Item with the same SKU already exists." in res )
      //    alert('message:Item with the same SKU already exists.');
      // else
      //    alert('added sucessfully')
    });
  }

  updateitem(){

  var val ={id:this.id,
            // Sno:this.Sno,
            ItemName:this.ItemName,
            ItemCode:this.ItemCode,
            SKU:this.SKU,
            ReferralCode:"w"
          };

    this.service.updateitems(val.id,val).subscribe(res=>{
      console.log(res)
    alert(res.toString());
    });
  }

  refreshItemList() {
    console.log("Refresh after update ")
    // You can add your code here to emit an event or perform any necessary actions after an update.
  }


}