//
//  DataViewController.h
//  MET
//
//  Created by Felix Wong on 4/14/14.
//  Copyright (c) 2014 My Endurance Trainer (MET). All rights reserved.
//

#import <UIKit/UIKit.h>

@interface DataViewController : UIViewController

@property (strong, nonatomic) IBOutlet UILabel *dataLabel;
@property (strong, nonatomic) id dataObject;

@end
