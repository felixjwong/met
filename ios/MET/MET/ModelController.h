//
//  ModelController.h
//  MET
//
//  Created by Felix Wong on 4/14/14.
//  Copyright (c) 2014 My Endurance Trainer (MET). All rights reserved.
//

#import <UIKit/UIKit.h>

@class DataViewController;

@interface ModelController : NSObject <UIPageViewControllerDataSource>

- (DataViewController *)viewControllerAtIndex:(NSUInteger)index storyboard:(UIStoryboard *)storyboard;
- (NSUInteger)indexOfViewController:(DataViewController *)viewController;

@end
